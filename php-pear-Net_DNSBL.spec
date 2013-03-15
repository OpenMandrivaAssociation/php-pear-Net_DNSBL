%define		_class		Net
%define		_subclass	DNSBL
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.4
Release:	4
Summary:	DNSBL Checker
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_DNSBL/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Checks if a given Host or URL is listed on an DNSBL or SURBL.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

# nuke useless(?) files
rm -rf %{buildroot}%{_datadir}/pear/data/Net_DNSBL/build.xml

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2012.0
+ Revision: 742138
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2
+ Revision: 679410
- mass rebuild

* Wed Dec 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-1mdv2011.0
+ Revision: 625910
- fix build
- 1.3.4

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-3mdv2011.0
+ Revision: 613722
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-2mdv2010.1
+ Revision: 468695
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Fri Jul 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2010.0
+ Revision: 394094
- update to new version 1.3.3

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 383554
- update to new version 1.3.2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.1
+ Revision: 322375
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdv2009.0
+ Revision: 278931
- update to new version 1.3.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdv2009.0
+ Revision: 236977
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2.1-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2008.0
+ Revision: 15814
- fix build
- 1.2.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdv2007.0
+ Revision: 82247
- Import php-pear-Net_DNSBL

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- 1.1.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

